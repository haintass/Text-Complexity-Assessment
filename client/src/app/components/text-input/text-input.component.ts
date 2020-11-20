import { Component, EventEmitter, Output } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
    selector: 'text-input-component',
    templateUrl: './text-input.component.html',
    styleUrls: ['./text-input.component.css']
})
export class TextInputComponent {
    @Output() onTextProcessing = new EventEmitter<boolean>();

    textForProcessing: string = null;

    alertWarningVisibility: boolean = false;
    errorMessage: string;
    alertType: string = 'alert-warning';

    constructor(private http: HttpClient){ }

    processText() {
        if (!this.textForProcessing || this.textForProcessing.length < 1) {
            this.alertWarningVisibility = true;
            this.errorMessage = 'errors.textNotFound'
        }
        else {
            this.onTextProcessing.emit(true);

            this.http.post('api/processText', this.textForProcessing)
            .subscribe(
                response => {
                    console.log('success: ' + response);

                    this.onTextProcessing.emit(false);
                },
                response => {
                    this.alertWarningVisibility = true;
                    this.errorMessage = response.error.errorType;
                    this.alertType = 'alert-danger';

                    this.onTextProcessing.emit(false);
                }
            )
        }
    }

    onHideAlert(){
        this.alertWarningVisibility = false;
      }
}