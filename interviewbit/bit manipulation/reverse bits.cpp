unsigned int Solution::reverse(unsigned int A) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details

    for (unsigned int k=0; k < 16; ++k) {
        unsigned int mr {(unsigned int)1<<k};
        unsigned int ml {((unsigned int)0x80000000)>>k};
        unsigned int r {A&mr};
        unsigned int l {A&ml};
        
        if (r == 0 && l != 0)
            A -= l;
        else if (r != 0 && l == 0)
            A += ml;
        if (l == 0 && r != 0)
            A -= r;
        else if (l != 0 && r == 0)
            A += mr;
        
    }
    
    return A;
}
