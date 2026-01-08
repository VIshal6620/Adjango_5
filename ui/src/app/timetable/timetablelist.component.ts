import { Component } from '@angular/core';
import { BaseListCtl } from '../base-list.component';
import { ActivatedRoute } from '@angular/router';
import { ServiceLocatorService } from '../service-locator.service';

@Component({
  selector: 'app-timetablelist',
  templateUrl: './timetablelist.component.html',
  styleUrls: ['./timetablelist.component.css']
})
export class TimetableListComponent extends BaseListCtl {
  constructor(locator: ServiceLocatorService, route: ActivatedRoute) {
          super(locator.endpoints.TIMETABLE, locator, route);
        }
  

}