import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { PythonService } from '../services/python.service';


@Component({
  selector: 'app-navigation',
  templateUrl: './navigation.component.html',
  styleUrl: './navigation.component.css'
})
export class NavigationComponent {

  constructor(private router: Router,
    private service: PythonService
  ) { }

  goHome(): void {
    this.router.navigate(['home/home-page']);
  }

  goProfile(): void {
    this.router.navigate(['profile']);
  }

  goGameRegister(): void {
    this.router.navigate(['game-register'])
  }

}
