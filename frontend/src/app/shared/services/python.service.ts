import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Login, LoginResponse } from '../models/login.models';
import { Cadastro } from '../models/cadastro.model';
import { Jogo } from '../models/jogo.model';

@Injectable({
  providedIn: 'root'
})
export class PythonService {

  readonly API = 'http://127.0.0.1:5000';

  constructor(
    private http: HttpClient
  ) { }

  login(body: Login): Observable<any> {
    return this.http.post<any>(`${this.API}/login`, body);
  }

  storeUserData(user: LoginResponse): void {
    const { senhaUsuario, ...userWithoutSenha } = user;
    localStorage.setItem('user', JSON.stringify(userWithoutSenha));
  }

  cadastro(body: Cadastro): Observable<any> {
    return this.http.post<any>(`${this.API}/cadastro`, body);
  }

  getAllJogos(): Observable<any> {
    return this.http.get<any>(`${this.API}/jogos`);
  }

  insertJogo(body: Jogo): Observable<any> {
    return this.http.post<any>(`${this.API}/insert/jogos`, body);
  }
}
