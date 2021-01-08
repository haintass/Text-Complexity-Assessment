import { Component, EventEmitter, Output } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
    selector: 'text-input-component',
    templateUrl: './text-input.component.html',
    styleUrls: ['./text-input.component.css']
})
export class TextInputComponent {
    @Output() onTextProcessing = new EventEmitter<boolean>();
    @Output() onProcessingComplete = new EventEmitter<Number>();

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
            .toPromise()
            .then((res:any) => {
                this.textForProcessing = null;
                this.onProcessingComplete.emit(res.textComplexity);
            })
            .catch((ex:any) => {
                this.alertWarningVisibility = true;
                this.errorMessage = ex.error.errorType || 'errors.internalServerError';
                this.alertType = 'alert-danger';

                this.onTextProcessing.emit(false)
            });
        }
    }

    onHideAlert(){
        this.alertWarningVisibility = false;
      }
}