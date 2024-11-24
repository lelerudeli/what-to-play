import { Component } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Login } from '../../../shared/models/login.models';
import { BehaviorSubject } from 'rxjs';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {
  isLoginPageSelected: boolean = true;

  form: FormGroup = new FormGroup({
    email: new FormControl(null, Validators.required),
    senha: new FormControl(null, Validators.required),
  });

  isLoadingSubject: BehaviorSubject<boolean> = new BehaviorSubject(false);

  condicao: boolean = true

  constructor(
    private router: Router,
  ) {}

  authenticate(): void {
    this.isLoadingSubject.next(true);
  }

}
