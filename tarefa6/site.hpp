class Site{
        int *spin, *up, *down, *left, *right;
    public:
        void init(int (*)[L], int, int);
        int site_spin(){return *spin;};
        float site_energy();
};

void Site::init(int s[L][L], int i, int j){
    up = &s[(i+L-1)%L][j];
    down = &s[(i+1)%L][j];
    left = &s[i][(j+L-1)%L];
    right = &s[i][(j+1)%L];
    spin = &s[i][j];
}

float Site::site_energy(){
    float neighbors = (*up + *down + *left + *right);
    return *spin * 0.5 * neighbors;
}
