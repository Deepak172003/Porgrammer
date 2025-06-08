document.getElementById('resultForm').addEventListener('submit', function (e) {
  e.preventDefault();

  const name = document.getElementById('name').value;
  const roll = document.getElementById('roll').value;
  const math = parseInt(document.getElementById('math').value);
  const sci = parseInt(document.getElementById('science').value);
  const eng = parseInt(document.getElementById('english').value);

  const total = math + sci + eng;
  const percentage = ((total / 300) * 100).toFixed(2);
  let grade = '';

  if (percentage >= 80) grade = 'A';
  else if (percentage >= 60) grade = 'B';
  else if (percentage >= 40) grade = 'C';
  else grade = 'Fail';

  document.getElementById('output').innerHTML = `
    <h3>Result for ${name} (Roll No: ${roll})</h3>
    <p>Total Marks: ${total}/300</p>
    <p>Percentage: ${percentage}%</p>
    <p>Grade: ${grade}</p>
  `;
});