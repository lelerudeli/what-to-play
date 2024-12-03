import { Injectable } from '@angular/core';
import { ToastrService } from 'ngx-toastr';

@Injectable({
  providedIn: 'root',
})
export class AlertService {

  constructor(private toastr: ToastrService) { }

  showSucessMessage(message: string = 'Dados Salvos com Sucesso!') {
    this.toastr.success(message, '');
  }


  showErrorMessage(message = null) {
    this.toastr.error(message || 'Algum erro ocorreu!');
  }

  showWarningMessage(message = null) {
    this.toastr.warning(message || 'Algum erro ocorreu!');
  }
}