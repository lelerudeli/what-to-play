import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { ForgetPasswordComponent } from './forget-password/forget-password.component';
import { AuthenticationRoutingModule } from './autenthication-routing.module';

@NgModule({
  declarations: [
    LoginComponent,
    ForgetPasswordComponent,
    RegisterComponent
  ],
  imports: [
    AuthenticationRoutingModule,
    CommonModule
  ],
  providers: [],
  bootstrap: []
})
export class AuthenticationModule { }