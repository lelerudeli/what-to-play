import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PythonService {

  readonly API = 'http://127.0.0.1:5000'

  constructor(
    private http: HttpClient
  ) { }

  getAll(): Observable<void> {
    return this.http.get<void>(this.API);
  }
}
