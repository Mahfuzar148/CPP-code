#include<bits/stdc++.h>
using namespace std;
int main()
{
    
    string s = "abcde";
    ///substring print using substring function
    for(int i=0;i<5;i++)
    {
        for(int j=i;j<5;j++)
        {
            cout<<i<<" "<<j-i+1<<" ";
            cout<<s.substr(i,j-i+1)<<endl;
        }
    }
  ///substring print using only for loop
    for(int i=0;i<5;i++)
    {
        for(int j=i+1;j<=5;j++)
        {
            for(int k=i;k<j;k++)
                cout<<s[k];
            cout<<endl;
        }
    }
    return 0;

}
