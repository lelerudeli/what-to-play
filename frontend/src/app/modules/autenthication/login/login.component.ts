import { Component } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { BehaviorSubject, first, Observable, of } from 'rxjs';
import { Router } from '@angular/router';
import { PythonService } from '../../../shared/services/python.service';
import { HttpErrorResponse } from '@angular/common/http';
import { LoginResponse } from '../../../shared/models/login.models';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
})
export class LoginComponent {
  isLoginPageSelected: boolean = true;

  form: FormGroup = new FormGroup({
    emailUsuario: new FormControl(null, [
      Validators.required,
      Validators.email,
    ]),
    senhaUsuario: new FormControl(null, Validators.required),
  });

  isLoadingSubject: BehaviorSubject<boolean> = new BehaviorSubject(false);

  constructor(private router: Router, private service: PythonService) {}

  authenticate(): void {
    this.isLoadingSubject.next(true);

    const credentials = {
      username: this.form.value.emailUsuario,
      password: this.form.value.senhaUsuario,
    };

    this.service
      .getAll(credentials) // Passando as variáveis corretas
      .pipe(first())
      .subscribe({
        next: (login: LoginResponse) => {
          this.service.storeUserData(login);
          this.isLoadingSubject.next(false);
          this.router.navigate(['home/home-page']);
        },
        error: (error: HttpErrorResponse) => {
          console.log('ocorreu um erro', error);
          this.isLoadingSubject.next(false);
        },
      });
  }
}
