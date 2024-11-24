import { Component, EventEmitter, Output } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';

@Component({
  selector: 'app-forgot-password',
  templateUrl: './forgot-password.component.html',
  styleUrl: './forgot-password.component.css'
})
export class ForgotPasswordComponent {

  @Output()
  back: EventEmitter<void> = new EventEmitter();

  emailControl = new FormControl(null, Validators.required);

  resetPassword(): void {
    this.back.emit();
  }

}
