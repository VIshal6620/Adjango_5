import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MarksheetlistComponent } from './marksheetlist.component';

describe('MarksheetlistComponent', () => {
  let component: MarksheetlistComponent;
  let fixture: ComponentFixture<MarksheetlistComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [MarksheetlistComponent]
    });
    fixture = TestBed.createComponent(MarksheetlistComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
