import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Login, LoginResponse } from '../models/login.models';

@Injectable({
  providedIn: 'root'
})
export class PythonService {

  readonly API = '/api'

  constructor(
    private http: HttpClient
  ) { }

  getAll(): Observable<any> {
    return this.http.get<any>(`${this.API}/`, {
      responseType: 'text' as 'json'
    });
  }

  
  storeUserData(user: LoginResponse): void {
    const { senha, ...userWithoutSenha } = user;
    localStorage.setItem('user', JSON.stringify(userWithoutSenha));
  }
}
