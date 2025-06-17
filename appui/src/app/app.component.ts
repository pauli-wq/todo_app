import { Component } from "@angular/core";
import { CommonModule } from "@angular/common";
import { RouterOutlet } from "@angular/router";
import { FormsModule } from "@angular/forms";

@Component({
  standalone: true,
  imports: [CommonModule, RouterOutlet, FormsModule],
  selector: "app-root",
  templateUrl: "./app.component.html",
  styleUrls: ["./app.component.css"],
})
export class AppComponent {
  title = "my-app";
  newTask = "";
  tasks: string[] = [];
}
