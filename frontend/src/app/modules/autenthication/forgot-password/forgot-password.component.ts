import { Component, EventEmitter, Output } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { AlertService } from '../../../shared/services/alert-service/alert.service';

@Component({
  selector: 'app-forgot-password',
  templateUrl: './forgot-password.component.html',
  styleUrl: './forgot-password.component.css'
})
export class ForgotPasswordComponent {

  @Output()
  back: EventEmitter<void> = new EventEmitter();

  form = new FormGroup({
    emailControl: new FormControl(null, [Validators.required, Validators.email])
  });

  constructor(
    private alertService: AlertService
  ){}

  resetPassword(): void {
    this.alertService.showSucessMessage('Dados salvos!');
    this.back.emit();
  }

}
