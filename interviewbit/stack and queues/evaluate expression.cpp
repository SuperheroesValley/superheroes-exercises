pair<int, int> readExpr(vector<string> &A, int i)
{
    if (A[i] == "/" || A[i] == "+" || A[i] == "-" || A[i] == "*") {
        auto [e1, i1] = readExpr(A, i+1);
        auto [e2, i2] = readExpr(A, i1);
        if (A[i] == "/")
            return {e2/e1, i2};
        if (A[i] == "+")
            return {e2+e1, i2};
        if (A[i] == "-")
            return {e2-e1, i2};
        if (A[i] == "*")
            return {e2*e1, i2};
    } else
        return {stoi(A[i]), i+1};
}

int Solution::evalRPN(vector<string> &A) {
    reverse(A.begin(), A.end());
    return readExpr(A, 0).first;
}
