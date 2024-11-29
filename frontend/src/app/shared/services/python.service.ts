import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Login, LoginResponse } from '../models/login.models';

@Injectable({
  providedIn: 'root'
})
export class PythonService {

  readonly API = 'http://127.0.0.1:5000';

  constructor(
    private http: HttpClient
  ) { }

  getAll(): Observable<any> {
    return this.http.get<any>(`${this.API}/jogos`);
  }

  
  storeUserData(user: LoginResponse): void {
    const { senha, ...userWithoutSenha } = user;
    localStorage.setItem('user', JSON.stringify(userWithoutSenha));
  }
}
