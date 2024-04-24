/**
 * 
 * 
빈도수 세기- validAnagram
두 개의 문자열이 주어졌을 때, 두 번째 문자열이 첫 번째 문자열의 애너그램인지 확인하는 함수를 작성합니다. 애너그램은 다른 글자의 글자를 재배열하여 형성된 단어, 구 또는 이름입니다. (예시: cinema -> iceman)

예시:

validAnagram('', '') // true
validAnagram('aaz', 'zza') // false
validAnagram('anagram', 'nagaram') // true
validAnagram("rat","car") // false) // false
validAnagram('awesome', 'awesom') // false
validAnagram('amanaplanacanalpanama', 'acanalmanplanpamana') // false
validAnagram('qwerty', 'qeywrt') // true
validAnagram('texttwisttime', 'timetwisttext') // true
안내: 문자열에 소문자만 포함되어 있다고 가정해도 됩니다.

Time Complexity - O(n)

 */

const validAnagram = (str1, str2) => {
  // 만약 두 문자열의 길이가 다르면 false
  if (str1.length !== str2.length) return false;
  // 만약 두 문자열이 ''라면 true
  if (str1 === "" && str2 === "") return true;

  // str1과 str2를 순회하여 모두 각 객체에 담음
  const fc1 = {};
  const fc2 = {};

  for (let char of str1) {
    fc1[char] = (fc1[char] || 0) + 1;
  }

  for (let char of str2) {
    fc2[char] = (fc2[char] || 0) + 1;
  }

  //fc1과 fc2 객체의 모든 알파뱃과 그 개수를 비교함
  for (let char in fc1) {
    // 아예 fc2에 동일한 알파벳이 없다면 false
    if (!(char in fc2)) return false;
    // 개수가 일치하지 않는다면 false
    if (fc1[char] !== fc2[char]) return false;
  }

  return true;
  //모든 케이스를 통과했으므로 true
};

console.log(validAnagram("", "")); // true
console.log(validAnagram("aaz", "zza")); // false
console.log(validAnagram("anagram", "nagaram")); // true
console.log(validAnagram("rat", "car")); // false)) // false
console.log(validAnagram("awesome", "awesom")); // false
console.log(validAnagram("amanaplanacanalpanama", "acanalmanplanpamana")); // false
console.log(validAnagram("qwerty", "qeywrt")); // true
console.log(validAnagram("texttwisttime", "timetwisttext")); // true
