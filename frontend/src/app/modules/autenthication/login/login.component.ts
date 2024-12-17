import { Component } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { BehaviorSubject, first } from 'rxjs';
import { Router } from '@angular/router';
import { PythonService } from '../../../shared/services/python.service';
import { HttpErrorResponse } from '@angular/common/http';
import { LoginResponse } from '../../../shared/models/login.models';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent{
  isLoginPageSelected: boolean = true;

  form: FormGroup = new FormGroup({
    emailUsuario: new FormControl(null, [Validators.required, Validators.email]),
    senhaUsuario: new FormControl(null, Validators.required),
  });

  isLoadingSubject: BehaviorSubject<boolean> = new BehaviorSubject(false);

  constructor(
    private router: Router,
    private service: PythonService,
    private toast: ToastrService
  ) {}

  authenticate(): void {
    this.isLoadingSubject.next(true);
    this.service.login(this.form.value)
      .pipe(first())
      .subscribe({
        next: (login: LoginResponse) => {
          this.service.storeUserData(login);
          this.isLoadingSubject.next(false);
          this.toast.success('Bem vindo ao "What To Play?"');
          this.router.navigate(['home/home-page']);
        },
        error: (error: HttpErrorResponse) => {
          this.toast.error('Usuário ou senha inválidos');
          this.isLoadingSubject.next(false);
        },
      });
  }

}
