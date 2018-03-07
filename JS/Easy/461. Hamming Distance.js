/**
 * @param {number} x
 * @param {number} y
 * @return {number}
 */
var hammingDistance = function(x, y) {
    var orx = x ^ y;
    var ans = 0;
    while (orx) {
        orx &= (orx - 1);
        ++ans;
    }
    return ans;
};