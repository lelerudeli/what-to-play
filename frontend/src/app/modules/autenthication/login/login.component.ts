import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { BehaviorSubject } from 'rxjs';
import { Router } from '@angular/router';
import { PythonService } from '../../../shared/services/python.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent implements OnInit {
  isLoginPageSelected: boolean = true;

  form: FormGroup = new FormGroup({
    email: new FormControl(null, Validators.required),
    senha: new FormControl(null, Validators.required),
  });

  isLoadingSubject: BehaviorSubject<boolean> = new BehaviorSubject(false);

  condicao: boolean = true

  constructor(
    private router: Router,
    private service: PythonService
  ) {}

  ngOnInit(): void {
    this.service.getAll();
  }

  authenticate(): void {
    this.isLoadingSubject.next(true);
  }

}
