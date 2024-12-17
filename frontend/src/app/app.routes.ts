import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { isAuthenticatedGuard } from './shared/guards/auth.guard';
import { ProfileComponent } from './modules/profile/profile.component';

export const routes: Routes = [
  {
    path: 'authentication',
    loadChildren: () =>
      import('./modules/autenthication/autenthications.module').then(
        (m) => m.AuthenticationModule
      )
  },
  {
    path: 'home',
    canActivate: [isAuthenticatedGuard],
    loadChildren: () =>
      import('./core/core-module').then(
        (m) => m.CoreModule
      ),
  },
  {
    path: 'all-games',
    loadChildren: () =>
      import('./modules/all-games/all-games.module').then(
        (m) => m.AllGamesModule
      )
  },
  {
    path: 'profile',
    loadChildren: () =>
      import('./modules/profile/profile.module').then(
        (m) => m.ProfileModule
      )
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