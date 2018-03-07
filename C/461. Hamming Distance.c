int hammingDistance(int x, int y) {
    int orx = x ^ y;
    int num = 0;
    while (orx) {
        orx &= (orx - 1);
        ++num;
    }
    return num;
}