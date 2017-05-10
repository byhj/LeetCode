/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    var num = 0;
    for (var val in nums) {
        num ^= val;
    }
    return num;
};