import { Component } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { BehaviorSubject } from 'rxjs';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrl: './register.component.css'
})
export class RegisterComponent {
  isLoginPageSelected: boolean = false;

  form: FormGroup = new FormGroup({
    nome: new FormControl(null, Validators.required),
    email: new FormControl(null, Validators.required),
    senha: new FormControl(null, Validators.required),
  });

  isLoadingSubject: BehaviorSubject<boolean> = new BehaviorSubject(false);

  condicao: boolean = true

  constructor(
    private router: Router,
  ) {}

}
