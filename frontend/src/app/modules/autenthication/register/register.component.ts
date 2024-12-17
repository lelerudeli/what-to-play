import { Component } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { BehaviorSubject, first } from 'rxjs';
import { Router } from '@angular/router';
import { PythonService } from '../../../shared/services/python.service';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrl: './register.component.css'
})
export class RegisterComponent {
  isLoginPageSelected: boolean = false;

  form: FormGroup = new FormGroup({
    nomeUsuario: new FormControl(null, Validators.required),
    nomeCompleto: new FormControl(null, Validators.required),
    emailUsuario: new FormControl(null, [Validators.required, Validators.email]),
    dataNascimento: new FormControl(null, Validators.required),
    senhaUsuario: new FormControl(null, Validators.required),
  });

  isLoadingSubject: BehaviorSubject<boolean> = new BehaviorSubject(false);

  constructor(
    private pythonService: PythonService,
    private router: Router,
    private toast: ToastrService
  ) { }

  register(): void {
    this.isLoadingSubject.next(true);
    this.pythonService.cadastro(this.form.value).pipe(
      first()
    ).subscribe({
      next: () => {
        this.toast.success('Usuário cadastrado com sucesso!');
        this.router.navigate(['home/home-page']);
        this.isLoadingSubject.next(false);
      },
      error: () => {
        this.toast.error('Email já cadastrado!');          
      },
    }
    );
  }

}
