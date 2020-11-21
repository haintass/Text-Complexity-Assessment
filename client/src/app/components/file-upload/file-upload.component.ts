import { Component, Output, EventEmitter } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FileTypes } from 'src/app/common/global-constants';

@Component({
  selector: 'file-upload-component',
  templateUrl: './file-upload.component.html',
  styleUrls: ['./file-upload.component.css']
})
export class FileUploadComponent { 
    @Output() onTextProcessing = new EventEmitter<boolean>();

    alertWarningVisibility: boolean = false;
    errorMessage: string;
    alertType: string;
  
    fileUploadInput: any = null;
    fileToUpload: File = null;
    formData: FormData = null;

    constructor(private http: HttpClient){ }

    handleFileInput(files: FileList, fileUploadInput:any) {
        this.fileToUpload = files.item(0);
        this.fileUploadInput = fileUploadInput;
    }

    clearFile(event: Event){
        this.fileToUpload = null;
        this.fileUploadInput.clear(event);
    }

    uploadFile(){
        if (!this.fileToUpload){
            return;
        }

        if (this.fileToUpload.type != FileTypes.txt) {
            this.alertWarningVisibility = true;
            this.errorMessage = 'errors.incorrectFileExtension';
            this.alertType = 'alert-warning'
        }
        else {
            this.formData = new FormData();
            this.formData.append('uploadedUserFile', this.fileToUpload, this.fileToUpload.name);

            this.onTextProcessing.emit(true);
          
            this.http.post('/api/processFile', this.formData)
            .toPromise()
            .then((res:any) => {
                this.fileUploadInput.clear();
                this.fileToUpload = null;
            })
            .catch((ex:any) => {
                this.alertWarningVisibility = true;
                this.errorMessage = ex.error.errorType;
                this.alertType = 'alert-danger';
            })
            .finally(() => this.onTextProcessing.emit(false))
        }
    }

    onHideAlert(){
        this.alertWarningVisibility = false;
      }
}