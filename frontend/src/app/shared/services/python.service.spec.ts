import { TestBed } from '@angular/core/testing';

import { PythonService } from './python.service';

describe('PythonService', () => {
  let service: PythonService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PythonService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
