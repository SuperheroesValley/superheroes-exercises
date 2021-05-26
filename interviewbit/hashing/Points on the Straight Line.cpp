int Solution::maxPoints(vector<int> &A, vector<int> &B) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    
    map<tuple<int, int, int>, int> cont;
    map<pair<int, int>, int> molt; // how many times a point occurs
    int best {0};
    map<int, int> xCount;
    int N = (int)A.size();
    
    vector<int> toDelete;
    int off{0};
    
    for (int k=0; k < N; ++k) {
        ++molt[{A[k], B[k]}];
        if (molt[{A[k], B[k]}] > 1) { // remove duplicates
            toDelete.push_back(k-off);
            ++off;
        }
    }
    
    for (auto &x : toDelete) {
        A.erase(A.begin()+x);
        B.erase(B.begin()+x);
    }
    N -= off;
    
    // y = (m1/m2)*x + (q1/q2)   con m1,m2,q1,q2 interi
    // m2*q2*y - m1*q2*x - q1*m2 = 0
    // a*y + b*x + c = 0
    // a = m2*q2     b = -m1*q2    c = -q1*m2
    for (int k = 0; k < N; ++k) {
        int moltK = molt[{A[k], B[k]}];
        if (moltK > 1) {
            xCount[A[k]] += moltK*(moltK-1)/2;
            best = max(best, xCount[A[k]]);
        }
        
        for (int j = k+1; j < N; ++j) {
            int moltJ = molt[{A[j], B[j]}];
            // c = -ky -kx*b
            // jy + jx*b - (ky + kx*b) = 0
            // jy - ky + b*(jx - kx) = 0
            // b = (ky - jy)/(jx - kx)
            
            // removing the fractional part
            
            // c = - (ky + kx*(ky - jy)/(jx - kx))
            // c = - (ky*(jx - kx) + kx*(ky - jy))/(jx - kx)
            // c = - (ky*jx - kx*jy)/(jx - kx)
            
            // the equation of the line will be
            // (jx - kx)*y = (ky - jy)*x - (ky*jx - kx*jy)
            // or
            // (jx - kx)*y - (ky - jy)*x + (ky*jx - kx*jy) = 0
            
            // check if on the same x axis
            if (A[k] == A[j]) {
                xCount[A[k]] += moltK*moltJ;
                best = max(best, xCount[A[k]]);
                continue;
            }
            
            int a = A[j] - A[k];
            int b = -(B[k] - B[j]);
            int c = B[k]*A[j] - A[k]*B[j];
            
            // normalize it
            int g = __gcd(a, b);
            if (g != 1)
                g = __gcd(g, c);
            a /= g;
            b /= g;
            c /= g;
            
            if (cont[{a, b, c}] == 0)
                cont[{a, b, c}] = moltK*(moltK-1)/2;
            cont[{a, b, c}] += moltK*moltJ;
            //~ cout << A[k] << " " << B[k] << " " << A[j] << " " << B[j] << endl;
            //~ cout << a << " " << b << " " << c << " " << cont[{a, b, c}] << endl;
            best = max(best, cont[{a, b, c}]);
        }
    }
    
    //~ cout << best << endl;
    
    int number_of_pairs = best;
    
    // if we have n pairs of points on the same line than we have K points with coeff_bin(K, 2) = n
    // hence
    // K*(K-1)/2 = n
    // K*K - K - 2*n = 0
    // K = ( 1 + sqrt(1 + 8*n) )/ 2
    
    if (number_of_pairs == 0)
        return (N == 0 ? 0 : 1);
    
    int sol = (1 + round(sqrt(8*number_of_pairs + 1)))/2;
    //~ cout << 8*number_of_pairs + 1 << endl;
    
    return sol;
}


// Easier solution
int Solution::maxPoints(vector<int> &A, vector<int> &B) {
    int N = (int)A.size();
    
    int best{0};
    
    for (int k=0; k < N; ++k) {
        map<pair<int, int>, int> cont;
        int overlap {1};
        int currBest{0};
        for (int j=k+1; j < N; ++j) {
            if (A[k] == A[j] && B[k] == B[j])
                ++overlap;
            else {
                pair<int, int> slope {B[j] - B[k], A[j] - A[k]};
                int g = __gcd(slope.first, slope.second); // gcd(A, 0) == A
                slope.first /= g;
                slope.second /= g;
                
                ++cont[slope];
                currBest = max(currBest, cont[slope]);
            }
        }
        
        best = max(best, currBest + overlap);
    }
    
    return best;
}
