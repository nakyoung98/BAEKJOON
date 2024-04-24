/**
 * 두 개의 배열을 인자로 받는 same 함수를 구현하시오.
 * 만약 두번째 배열의 모든 원소가 첫번째 배열에 존재하는 원소의 제곱이며,
 * 첫번째 배열 내에 동일한 값의 원소개 여러 개 존재할 경우
 * 두번째 배열에서도 해당 원소의 제곱인 원소가 동일한 개수만큼 존재한다면 true 를 반환한다.
 * 아니라면 false를 반환한다.
 */

/**
 * [1,2,3],[1,4,9] => true
 * [1,2,3],[1,4,4] => false
 * [1,2,3,3],[1,4,9,9] => true
 * [1,2,3,3],[1,4,4,9] => false
 * [1,2,3],[9,4,1] => true
 */

//sol1
/*
const same = (arr1, arr2) => {
  //두 배열의 크기가 같은지부터 비교한다
  if (arr1.length !== arr2.length) {
    //다르면 return
    return false;
  }

  //arr1의 모든 요소를 제곱한 배열 arr3를 만든다
  const arr3 = arr1.map((value) => value ** 2);
  //arr3를 정렬한다
  arr3.sort();
  //arr2도 정렬한다
  arr2.sort();
  //arr3과 arr2의 모든 요소를 비교한다 (루프)
  for (let i = 0; i < arr2.length; i++) {
    //만약 다른게 나타나면 false를 return한다
    if (arr3[i] !== arr2[i]) {
      return false;
    }
  }
  //true를 return한다
  return true;
};
*/

//sol2
const same = (arr1, arr2) => {
  //두 배열의 크기가 같은지부터 비교한다
  if (arr1.length !== arr2.length) {
    //다르면 return
    return false;
  }

  //frequency 기법을 사용하여 배열을 분리하여 객체에 담고, 개수를 추가한다
  const fc1 = {};
  const fc2 = {};

  //배열 순회 후 객체에 담기
  arr1.forEach((value) => (fc1[value] = (fc1[value] || 0) + 1));
  arr2.forEach((value) => (fc2[value] = (fc2[value] || 0) + 1));

  //fc1과 fc2 비교하기
  for (let key in fc1) {
    //fc1의 key를 제곱한 값이 fc2에 없으면
    if (!(key ** 2 in fc2)) {
      //false return
      return false;
    }
    //fc1의 key를 제곱한 값이 fc2에 있으나, 그 value가 다르다면(개수가 다르다면)
    if (fc1[key] !== fc2[key ** 2]) {
      //false return
      return false;
    }
  }

  return true;
};

console.log(same([1, 2, 3], [1, 4, 9]));
console.log(same([1, 2, 3], [1, 4, 4]));
console.log(same([1, 2, 3, 3], [1, 4, 9, 9]));
console.log(same([1, 2, 3, 3], [1, 4, 4, 9]));
console.log(same([1, 2, 3], [9, 4, 1]));
