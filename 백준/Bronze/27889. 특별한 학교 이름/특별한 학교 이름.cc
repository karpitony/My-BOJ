#include <iostream>
#include <string>
#include <map>

using namespace std;

int main(void) {
    cin.tie(nullptr);
    cout.tie(nullptr);
    ios::sync_with_stdio(false);

    map<string, string> m;
    m.insert(make_pair("NLCS","North London Collegiate School")); 
    m.insert(make_pair("BHA","Branksome Hall Asia"));
    m.insert(make_pair("KIS","Korea International School"));
    m.insert(make_pair("SJA","St. Johnsbury Academy"));

    string name;
    cin >> name;
    cout << m[name] << "\n";

    return 0;
}