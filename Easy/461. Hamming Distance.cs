public class Solution {
    public int HammingDistance(int x, int y) {
        int orx = x ^ y;
        int ans = 0;
        while (orx != 0) {
            orx &= (orx - 1);
            ++ans;
        }
        return ans;
    }
}