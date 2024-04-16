  const fs = require("fs");
  const rawInput = fs.readFileSync('dev/stdin').toString();
  let Inputs = rawInput.split(/\n/g);

  //학생 수
  const StudentNum = +Inputs[0];
  Inputs.forEach((Input, i, arr) => (arr[i] = Input.split(/ /g)));
  Inputs = Inputs.slice(1, StudentNum+1);

  // 같은 반이었던 학생을 기록하는 배열
  const Students = [];
  for (let student = 0; student < StudentNum; student++) {
    Students.push(new Set());
  }

  //1학년부터 5학년까지 반복
  for (let i = 0; i < 5; i++) {
    // 반 리스트 만들기
    const Classes = [];
    for (let i = 0; i <= 9; i++) {
      Classes.push([]);
    }

    // 학생 수만큼 반복
    for (let j = 0; j < StudentNum; j++) {
      //j학생이 i학년일 때 반 번호
      const studentClass = +Inputs[j][i];

      //j학생을 해당 반에 추가
      Classes[studentClass].push(j);
    }

    //학생 수만큼 반복
    for (let student = 0; student < StudentNum; student++) {
      //본인 반 가지고 오기
      const studentClass = +Inputs[student][i];
      //본인 반의 친구들을 기록 배열에 추가하기
      const Class = Classes[studentClass];
      Class.forEach((classMate) => (classMate !== student ? Students[student].add(classMate) : null));
    }
  }

  const Nums = Students.map((value) => value.size);
  //최대 값
  const maxValue = Math.max(...Nums);
  const Result = Nums.findIndex((value) => value === maxValue);
  
  //임시 반장 선출 (1부터 시작하므로 +1 해야함)
  console.log(Result+1);