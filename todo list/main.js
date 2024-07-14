document.addEventListener('DOMContentLoaded', function() {
    const taskInput = document.getElementById('taskInput');
    const addButton = document.getElementById('addButton');
    const taskList = document.getElementById('taskList');
    let tasks = [];

    function addTask() {
        const taskName = taskInput.value.trim();

        if (taskName !== '') {
            tasks.push({ name: taskName, completed: false });
            taskInput.value = ''; 

    
            displayTasks();
        } else {
            alert("Please enter a valid task.");
        }
    }

    function removeTask(index) {
        tasks.splice(index, 1);
        displayTasks();
    }

  
    function completeTask(index) {
        tasks[index].completed = true;
        displayTasks();
    }

    
    function displayTasks() {
        taskList.innerHTML = ''; 

        tasks.forEach((task, index) => {
            const li = document.createElement('li');
            li.innerHTML = `
                <input type="checkbox" ${task.completed ? 'checked' : ''} onclick="completeTask(${index})">
                <span style="text-decoration: ${task.completed ? 'line-through' : 'none'}">${task.name}</span>
                <button onclick="removeTask(${index})">Remove</button>
            `;
            taskList.appendChild(li);
        });
    }

   
    taskInput.addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            addTask();
        }
    });

    addButton.addEventListener('click', addTask);
});
