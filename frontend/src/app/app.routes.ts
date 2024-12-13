import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { isAuthenticatedGuard } from './shared/guards/auth.guard';

export const routes: Routes = [
  {
    path: 'authentication',
    loadChildren: () =>
      import('./modules/autenthication/autenthications.module').then(
        (m) => m.AuthenticationModule
      )
  },
  {
    path: 'core',
    canActivate: [isAuthenticatedGuard],
    loadChildren: () =>
      import('./core/core-module').then(
        (m) => m.CoreModule
      ),
  },
  {
    path: '**',
    redirectTo: 'authentication/login'
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }