import { RouterModule, Routes } from '@angular/router';
import { isAuthenticatedGuard } from './shared/guards/auth.guard';
import { NgModule } from '@angular/core';

export const routes: Routes = [
    {
        path: 'authentication',
        loadChildren: () =>
          import('./module/autenthication/autenthication.module').then(
            (m) => m.AuthenticationModule
          )
      },
      {
        path: 'home',
        canActivate: [isAuthenticatedGuard],
        loadChildren: () =>
          import('./core/core.module').then(
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
