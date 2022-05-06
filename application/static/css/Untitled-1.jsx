/* 
  1. Store correct answers
   - When quiz begins, no answers are correct
*/
function quiz(){
  let score = 0 
  const question1 = window.prompt('What is today?')
  const answer1 = Date.getDay()
    if (question1 == answer1){
      score += 1
    };
  const question2 = window.prompt('What is 5 multipled by 5 evaluate to?')
  const answer2 = 25
    if (question2 == answer2){
      score += 1
    };
  const question3 = window.prompt('What is 5 multipled by 5 evaluate to?')
  
if (question3 == answer2){
  score += 1
};
  const question4 = window.prompt('What is 5 multipled by 5 evaluate to?')
  
if (question4 == answer2){
  score += 1
}; 
  const question5 = window.prompt('What is 5 multipled by 5 evaluate to?')
  
if (question5 == answer2){
  score += 1
};
  return score
  }
// 2. Store the rank of a player


// 3. Select the <main> HTML element

const element = Document.getElementsByTagName('main')
/*
  4. Ask at least 5 questions
   - Store each answer in a variable
   - Keep track of the number of correct answers
*/
//const question1 = window.prompt('What is today?')
//const answer1 = Date.getDay()



//const question2 = window.prompt('What is 5 multipled by 5 evaluate to?')
//const answer2 = 25


if (question2 == answer2){
  score += 1
};

console.log(score)
/*
  5. Rank player based on number of correct answers
   - 5 correct = Gold
   - 3-4 correct = Silver
   - 1-2 correct = Bronze
   - 0 correct = No crown
*/
const rank = ''
if(score > 4){
  rank = 'Gold'
} else if( score < 4 && score > 2){
  rank = 'Silver'} 
  else { rank = 'Bronze' }

// 6. Output results to the <main> element
Document.element.innerHTML = `<H1> Thanks For Playing! Your Score is ${score}, you ranked in the ${rank}!`