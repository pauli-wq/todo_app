import { Component, OnInit } from "@angular/core";
import { ApiService, Todo } from "../services/api.service";
import { FormsModule } from "@angular/forms";
import { CommonModule } from "@angular/common";

@Component({
  selector: "app-todo-list",
  templateUrl: "./todo-list.component.html",
  imports: [CommonModule, FormsModule],
  styleUrls: ["./todo-list.component.css"],
  providers: [ApiService],
})
export class TodoListComponent implements OnInit {
  todos: any[] = [];
  newTodo: Omit<Todo, "id"> = { title: "", description: "", completed: false };

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    this.loadTodos();
  }

  loadTodos(): void {
    this.apiService.getTodos().subscribe((todos: Todo[]) => {
      this.todos = todos;
    });
  }

  addTodo(): void {
    this.apiService.createTodo(this.newTodo).subscribe(() => {
      this.loadTodos();
      this.newTodo = { title: "", description: "", completed: false };
    });
  }

  toggleComplete(todo: Todo): void {
    this.apiService
      .updateTodo(todo.id, { completed: !todo.completed })
      .subscribe(() => this.loadTodos());
  }

  deleteTodo(id: number): void {
    this.apiService.deleteTodo(id).subscribe(() => this.loadTodos());
  }
}
