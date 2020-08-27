#include "iostream"
#include "vector"

using namespace std;

struct edge
{
    int a, b, cost;
};

int n, m, v;
vector<edge> e;
const int INF = 1000000000;

void solve()
{
    vector<int> d (n, INF);
    d[v] = 0;
    while (true)  {
        bool any = false;

        for (int j=0; j<m; ++j)
            if (d[e[j].a] < INF)
                if (d[e[j].b] > d[e[j].a] + e[j].cost)
                {
                    d[e[j].b] = d[e[j].a] + e[j].cost;
                    any = true;
                }

        if (!any) break;
    }
    cout << "\n Final Cost of Vertices from Starting Vertice " << v << ": ";
    for (auto x: d) {
        cout << x << " ";
    }
}

int main(int argc, char const *argv[]) {
    int a, b, cost;

    cout << "\n Name: Shivam Tawari";
    cout << "\n Roll no: A-58 Section: A";

    cout << "\n Enter Total Vertices: ";
    cin >> n;
    cout << " Enter Total Edges: ";
    cin >> m;

    for (int i=0; i<m; i++) {
        cout << " Enter start, end and cost of edge " << i+1 << ": ";
        cin >> a >> b >> cost;
        e.push_back({a, b, cost});
    }

    cout << " Enter starting vertex: ";
    cin >> v;

    solve();

    return 0;
}
