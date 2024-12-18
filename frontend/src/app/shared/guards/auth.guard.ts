import { inject } from '@angular/core';
import {jwtDecode} from 'jwt-decode';
import { ActivatedRouteSnapshot, CanActivateFn, Router, RouterStateSnapshot } from '@angular/router';

export const isAuthenticatedGuard: CanActivateFn = (
  next: ActivatedRouteSnapshot,
  state: RouterStateSnapshot) => {
    return isAuthenticated() 
      ? true : 
      inject(Router).createUrlTree(['authentication/login']);
}

  export function isAuthenticated(): boolean {
    const token = localStorage.getItem('token'); // Verifica se o token está armazenado
    if (!token) {
      console.error('Token não encontrado no localStorage!');
      return false; // Retorna falso se não houver token
    }
  
    try {
      const decoded: any = jwtDecode(token); // Tenta decodificar o token
      const currentTime = Math.floor(Date.now() / 1000); // Tempo atual em segundos
      return decoded.exp > currentTime; // Retorna true se o token ainda não expirou
    } catch (error: any) {
      console.error('Erro ao decodificar o token:', error.message);
      return false; // Retorna falso se o token for inválido
    }
}

