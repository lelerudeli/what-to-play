import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { AuthenticationRoutingModule } from './autenthication-routing.module';
import { ReactiveFormsModule } from '@angular/forms';
import { ForgotPasswordComponent } from './forgot-password/forgot-password.component';
import { SharedModule } from '../../shared/shared.module';


@NgModule({
  declarations: [
    LoginComponent,
    ForgotPasswordComponent,
    RegisterComponent
  ],
  imports: [
    AuthenticationRoutingModule,
    ReactiveFormsModule,
    CommonModule,
    SharedModule
  ],
  providers: [],
  bootstrap: []
})
export class AuthenticationModule { }