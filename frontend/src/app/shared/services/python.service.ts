import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Login, LoginResponse } from '../models/login.models';
import { HttpClient } from '@angular/common/http';
import { catchError, tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root',
})
export class PythonService {
  readonly API = 'http://127.0.0.1:5000';

  constructor(private http: HttpClient) {}

  getAll(credentials: { username: string; password: string }): Observable<any> {
    return this.http.post<any>(`${this.API}/login`, credentials).pipe(
      tap((response) => {
        // Armazenar o token de acesso no localStorage
        localStorage.setItem('token', response.token);
      }),
      catchError((error) => {
        console.error('Erro ao fazer login:', error);
        return throwError(error);
      })
    );
  }
  storeUserData(user: LoginResponse): void {
    const { senhaUsuario, ...userWithoutSenha } = user;
    localStorage.setItem('user', JSON.stringify(userWithoutSenha));
  }
}
function throwError(error: any): any {
  throw new Error('Function not implemented.');
}
