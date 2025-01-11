document.getElementById('askQuestionForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const title = document.getElementById('questionTitle').value;
    const body = document.getElementById('questionBody').value;

    const questions = document.getElementById('questions');
    const questionDiv = document.createElement('div');
    questionDiv.innerHTML = `
        <h3>${title}</h3>
        <p>${body}</p>
        <button class="answer-button">回答</button>
        <button class="upvote-button">👍</button>
    `;
    questions.appendChild(questionDiv);

    document.getElementById('questionTitle').value = '';
    document.getElementById('questionBody').value = '';
// 为回答按钮添加事件监听器
const answerButton = questionDiv.querySelector('.answer-button');
const answerInput = document.createElement('input'); // 创建输入框
answerInput.type = 'text'; // 设置输入框类型为文本
answerInput.placeholder = '在这里输入你的回答...'; // 设置输入框占位符
answerInput.style.display = 'none'; // 默认隐藏输入框

let submitButton; // 声明提交按钮变量，以便在事件处理函数中访问

// 提交按钮点击事件处理函数
function handleAnswerSubmit() {
    // 获取输入框的值
    const userAnswer = answerInput.value;
    if (userAnswer.trim() !== '') { // 确保用户输入不为空
        // 创建一个新的div来显示每个回答
        const newAnswerDisplay = document.createElement('div');
        newAnswerDisplay.textContent = userAnswer;
        questionDiv.appendChild(newAnswerDisplay); // 将新的回答显示在页面上
        // 清空输入框以便下次输入
        answerInput.value = '';
        // 隐藏输入框和提交按钮
        answerInput.style.display = 'none';
        if (submitButton) {
            submitButton.style.display = 'none';
        }
    }
}

// 添加回答按钮事件
answerButton.addEventListener('click', function() {
    // 显示输入框和提交按钮
    answerInput.style.display = 'block';
    // 如果已经存在提交按钮，则不需要再次创建
    if (!submitButton) {
        submitButton = document.createElement('button');
        submitButton.textContent = '提交回答';
        submitButton.addEventListener('click', handleAnswerSubmit);
        questionDiv.appendChild(submitButton); // 将提交按钮添加到页面
    } else {
        submitButton.style.display = 'block'; // 如果提交按钮已存在，只需显示它
    }
});

// 将元素添加到页面
questionDiv.appendChild(answerInput);
questionDiv.appendChild(answerButton);

    // 为点赞按钮添加事件监听器
    const upvoteButton = questionDiv.querySelector('.upvote-button');
    let upvotes = 0;
    upvoteButton.addEventListener('click', function() {
        upvotes++;
        upvoteButton.textContent = `👍 ${upvotes}`;
    });
});