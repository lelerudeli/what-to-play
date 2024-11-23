import { inject } from '@angular/core';
import { ActivatedRouteSnapshot, CanActivateFn, Router, RouterStateSnapshot } from '@angular/router';

export const isAuthenticatedGuard: CanActivateFn = (
  next: ActivatedRouteSnapshot,
  state: RouterStateSnapshot) => {
    return isAuthenticated() 
      ? true : 
      inject(Router).createUrlTree(['authentication/login']);
}

export function isAuthenticated(): boolean {
    const user = localStorage.getItem('user');
    return !!user; 
  }