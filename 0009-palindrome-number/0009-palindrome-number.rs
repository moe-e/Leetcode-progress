impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        let word = x.to_string();
        
        let mut l = 0;
        let mut r = word.len();
        
        while l < r-1{
            if word[l..l+1] != word[r-1..r]{
                return false;
            }
            l = l+1;
            r = r-1;
        }
        
        return true;
        
    }
}