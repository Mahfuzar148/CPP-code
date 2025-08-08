import os, json, re, time, requests

LEETCODE_USERNAME = os.getenv("LEETCODE_USERNAME")  # e.g. david_miller
CODEFORCES_HANDLE = os.getenv("CODEFORCES_HANDLE")  # e.g. david_miller_cf
CODECHEF_HANDLE = os.getenv("CODECHEF_HANDLE")      # optional

# For LeetCode auth (needed for per-user AC status)
LEETCODE_SESSION = os.getenv("LEETCODE_SESSION")    # cookie value
LEETCODE_CSRF    = os.getenv("LEETCODE_CSRF")       # if using GraphQL; optional for legacy

PROBLEMS_JSON = "problems.json"
SHEET_MD = "practice_sheet.md"

def load_problems():
    with open(PROBLEMS_JSON, "r", encoding="utf-8") as f:
        return json.load(f)

def fetch_codeforces_solved(handle):
    # CF official API: get all submissions, filter by verdict=OK
    url = f"https://codeforces.com/api/user.status?handle={handle}&from=1&count=100000"
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    data = r.json()
    solved = set()
    if data.get("status") == "OK":
        for sub in data["result"]:
            if sub.get("verdict") == "OK":
                prob = sub.get("problem", {})
                key = (prob.get("contestId"), prob.get("index"))
                solved.add(key)
    return solved

def fetch_leetcode_solved(username):
    """
    Approach: use legacy endpoint /api/problems/all/ with LEETCODE_SESSION cookie.
    It returns per-problem 'status' for the logged-in user. We'll map by slug.
    """
    cookies = {}
    headers = {"User-Agent": "Mozilla/5.0"}
    if LEETCODE_SESSION:
        cookies["LEETCODE_SESSION"] = LEETCODE_SESSION
    # legacy endpoint (works when authenticated)
    url = "https://leetcode.com/api/problems/all/"
    r = requests.get(url, headers=headers, cookies=cookies, timeout=30)
    if r.status_code != 200:
        return set()
    j = r.json()
    solved = set()
    for it in j.get("stat_status_pairs", []):
        stat = it.get("stat", {})
        slug = stat.get("question__title_slug")
        status = it.get("status")  # "ac", "notac", None
        if status == "ac" and slug:
            solved.add(slug)
    return solved

def fetch_codechef_solved(handle):
    """
    Public stable API নেই। চাইলে Skip/Manual রাখি।
    বিকল্প: প্রোফাইল পেজ স্ক্র্যাপ/অথ—ToS sensitive. তাই default: empty set.
    """
    return set()

def update_sheet(solved_map):
    # Read markdown and replace Status
    with open(SHEET_MD, "r", encoding="utf-8") as f:
        lines = f.readlines()

    def set_status(line, solved):
        # replace final cell to | Solved | or | Unsolved |
        if solved:
            return re.sub(r"\|\s*Unsolved\s*\|", "| Solved |", line)
        else:
            return re.sub(r"\|\s*Solved\s*\|", "| Unsolved |", line)

    new = []
    for line in lines:
        m = re.match(r"\|\s*(\d+)\s*\|", line)
        if not m:
            new.append(line); continue
        num = int(m.group(1))
        new.append(set_status(line, num in solved_map))
    with open(SHEET_MD, "w", encoding="utf-8") as f:
        f.writelines(new)
    print("✅ practice_sheet.md updated.")

def main():
    probs = load_problems()
    solved_nums = set()

    # Codeforces
    if CODEFORCES_HANDLE:
        cf_solved = fetch_codeforces_solved(CODEFORCES_HANDLE)
        for p in probs["codeforces"]:
            key = (p["contestId"], p["index"])
            if key in cf_solved:
                solved_nums.add(p["num"])

    # LeetCode (needs LEETCODE_SESSION cookie)
    lc_solved = fetch_leetcode_solved(LEETCODE_USERNAME) if LEETCODE_USERNAME else set()
    for p in probs["leetcode"]:
        if p["slug"] in lc_solved:
            solved_nums.add(p["num"])

    # CodeChef (skipped by default)
    cc_solved = fetch_codechef_solved(CODECHEF_HANDLE) if CODECHEF_HANDLE else set()
    for p in probs["codechef"]:
        if p.get("code") in cc_solved:
            solved_nums.add(p["num"])

    update_sheet(solved_nums)

if __name__ == "__main__":
    main()
