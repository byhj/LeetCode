public class Solution {
    public string ReverseString(string s) {
        char [] arr = s.ToCharArray();
        Array.Reverse(arr);
        return new string(arr);
    }
}
