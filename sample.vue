<template>
  <div class="container">

    <nevron-header>
      <template #title>System Assets Configuration</template>
      <template #p></template>
    </nevron-header>

    <hr/>

    <form autocomplete="off" class="needs-validation" novalidate>
      <div class="row">
        <div class="col-md-4 mt-2">
          <p class="h6">Company Logo</p>
          <p>Select logo which will show in manager as brand</p>
        </div>
        <div class="col-md-8">
          <div class="card">
            <div class="card-body" style="background-color: #F8F8FB">
              <div class="row text-center">
                <vue-transmit
                  @success="sendReload"
                  dragClass="border-blur-upload"
                  uploadAreaClasses="border-upload"
                  style="width: 100%"
                  :clickable="false"
                  :params="{ mediaFolderId: 1 }"
                  sty
                  tag="section"
                  ref="uploader"
                  :url="getFilePath()"
                  :headers="getHeaders()"
                >
                  <div v-if="imageUrl === ''">
                    <img
                      class="pb-2 img-fluid"
                      src="../../../assets/logo.png"
                      alt=""
                      title=""
                      @click="getImages"
                    />
                    <p class="align-middle">
                      Drag photos here or
                      <button class="btn btn-link p-0 b-0" type="button" @click="getImages">
                        find images in Media library</button
                      >.
                    </p>
                  </div>
                  <div v-else>
                    <img class="pb-2" :src="contentUrl + imageUrl" alt="" title="" @click="getImages" style="max-width: 80%; max-height: 400px"/>
                    <p class="align-middle">
                      Drag photos here or
                      <button class="btn btn-link p-0 b-0" type="button" @click="getImages">
                        find images in Media library</button
                      >.
                    </p>
                  </div>
                </vue-transmit>
              </div>
              <div class="text-right">
                <a href="javascript:void(0)" class="btn btn-primary float-right" @click="updateSetting(logo.id, imageUrl)">Update Logo</a>
              </div>
            </div>
          </div>
        </div>
      </div>

      <hr/>

      <div class="row">
        <div class="col-md-4 mt-2">
          <p class="h6">Mobile Login Background</p>
          <p>This is mobile login background image we can dynamically change here.</p>
        </div>
        <div class="col-md-8">
          <div class="card">
            <div class="card-body" style="background-color: #F8F8FB">
              <div class="row text-center">
                <vue-transmit
                  @success="sendBackgroundReload"
                  dragClass="border-blur-upload"
                  uploadAreaClasses="border-upload"
                  style="width: 100%"
                  :clickable="false"
                  :params="{ mediaFolderId: 1 }"
                  sty
                  tag="section"
                  ref="uploader"
                  :url="getFilePath()"
                  :headers="getHeaders()"
                >
                  <div v-if="mobileLoginBackgrounImageUrl === ''">
                    <img
                      class="pb-2 img-fluid"
                      src="../../../assets/logo.png"
                      alt=""
                      title=""
                      @click="getBackgroundImages"
                    />
                    <p class="align-middle">
                      Drag photos here or
                      <button class="btn btn-link p-0 b-0" type="button" @click="getBackgroundImages">
                        find images in Media library</button
                      >.
                    </p>
                  </div>
                  <div v-else>
                    <img class="pb-2" :src="contentUrl + mobileLoginBackgrounImageUrl" alt="" title="" @click="getBackgroundImages" style="max-width: 80%; max-height: 400px"/>
                    <p class="align-middle">
                      Drag photos here or
                      <button class="btn btn-link p-0 b-0" type="button" @click="getBackgroundImages">
                        find images in Media library</button>.
                    </p>
                  </div>
                </vue-transmit>
              </div>
              <div class="text-right">
                <a href="javascript:void(0)" class="btn btn-primary float-right" @click="updateSetting(mobileLoginBackground.id, mobileLoginBackgrounImageUrl)">Update</a>
              </div>
            </div>
          </div>
        </div>
      </div>
      <hr/>

      <div class="row">
        <div class="col-md-4 mt-2">
          <p class="h6">Mobile App Logo</p>
          <p>Mobile App Logo to show on mobile application.</p>
        </div>
        <div class="col-md-8">
          <div class="card">
            <div class="card-body" style="background-color: #F8F8FB">
              <div class="row text-center">
                <vue-transmit
                  @success="sendMobileLogoReload"
                  dragClass="border-blur-upload"
                  uploadAreaClasses="border-upload"
                  style="width: 100%"
                  :clickable="false"
                  :params="{ mediaFolderId: 1 }"
                  sty
                  tag="section"
                  ref="uploader"
                  :url="getFilePath()"
                  :headers="getHeaders()"
                >
                  <div v-if="mobileLogoImageUrl === ''">
                    <img
                      class="pb-2 img-fluid"
                      src="../../../assets/logo.png"
                      alt=""
                      title=""
                      @click="getMobileLogoImages"
                    />
                    <p class="align-middle">
                      Drag photos here or
                      <button class="btn btn-link p-0 b-0" type="button" @click="getMobileLogoImages">
                        find images in Media library</button
                      >.
                    </p>
                  </div>
                  <div v-else>
                    <img class="pb-2" :src="contentUrl + mobileLogoImageUrl" alt="" title="" @click="getMobileLogoImages" style="max-width: 80%; max-height: 400px"/>
                    <p class="align-middle">
                      Drag photos here or
                      <button class="btn btn-link p-0 b-0" type="button" @click="getMobileLogoImages">
                        find images in Media library</button>.
                    </p>
                  </div>
                </vue-transmit>
              </div>
              <div class="text-right">
                <a href="javascript:void(0)" class="btn btn-primary float-right" @click="updateSetting(mobileLogo.id, mobileLogoImageUrl)">Update</a>
              </div>
            </div>
          </div>
        </div>
      </div>
      <hr/>

      <div class="row">
        <div class="col-md-4 mt-2">
          <p class="h6">Primary Company Color</p>
          <p>Select company colour to be used as the primarily colour of the application.</p>
        </div>
        <div class="col-md-8">
          <div class="card">
            <div class="card-body" style="background-color: #F8F8FB">
              <div class="row text-center" style="text-align: center">
                <div class="pull-left col-md-6">
                  <b>Select Color : &nbsp;&nbsp;</b> <input type="color" class="color-input" style="width: 130px" v-model="defaultbgColor" >
                </div>

                <div class="pull-right">
                  <b>Color : &nbsp;&nbsp;</b> <input type="text" class="color-input " v-model="defaultbgColor">
                </div>
              </div>
              <div class="text-right">
                <a href="javascript:void(0)" class="btn btn-primary float-right" @click="updateSetting(defaultBG.id, defaultbgColor)">Update</a>
              </div>
            </div>
          </div>
        </div>
      </div>
      <hr/>
      <div class="row">
        <div class="col-md-4 mt-2">
          <p class="h6">Secondary Company Colour</p>
          <p>Select company colour to be used as the secondary colour of the application.</p>
        </div>
        <div class="col-md-8">
          <div class="card">
            <div class="card-body" style="background-color: #F8F8FB">
              <div class="row text-center" style="text-align: center">
                <div class="pull-left col-md-6">
                  <b>Select Color : &nbsp;&nbsp;</b> <input type="color" class="color-input" style="width: 130px" v-model="secondarybgColor" >
                </div>

                <div class="pull-right">
                  <b>Color : &nbsp;&nbsp;</b> <input type="text" class="color-input " v-model="secondarybgColor">
                </div>
              </div>
              <div class="text-right">
                <a href="javascript:void(0)" class="btn btn-primary float-right" @click="updateSetting(secondaryBG.id, secondarybgColor)">Update</a>
              </div>
            </div>
          </div>
        </div>
      </div>
      <hr/>
    </form>
    <attach-image
      ref="image"
      @attach="attachWithImage"
      @makeDir="folderRequest"
      @close="$refs.image.$children[0].close()"
    />
    <attach-image
      ref="loginBackground"
      @attach="attachBackgroundWithImage"
      @makeDir="folderRequest"
      @close="$refs.loginBackground.$children[0].close()"
    />
    <attach-image
      ref="mobileLogo"
      @attach="attachMobileLogoWithImage"
      @makeDir="folderRequest"
      @close="$refs.mobileLogo.$children[0].close()"
    />
    <create-folder ref="create" @save="createFolder" @close="$refs.create.$children[0].close()" />
  </div>
</template>
<script lang="ts">
  import {Component, Vue} from 'vue-property-decorator';
  import stores from '@/stores';
  import NevronHeader from '@/components/NevronHeader.vue';
  import AttachImage from '@/modules/Media/Attach.vue';
  import CreateFolder from '@/modules/Media/CreateFolder.vue';
  import axiosInstance from '../../helpers/axios';
  import session from '@/stores/Session';
  import { Setting } from '@/stores/Setting';
  @Component({
    components: {
      AttachImage,
      NevronHeader,
      CreateFolder,
    },
  })
  export default class GeneralSetting extends Vue {
    logo: ISetting = new Setting();
    mobileLoginBackground: ISetting = new Setting();
    mobileLogo: ISetting = new Setting();
    defaultBG: ISetting = new Setting();
    secondaryBG: ISetting = new Setting();
    imageUrl: string = '';
    defaultbgColor: string = '';
    secondarybgColor: string = '';
    mobileLoginBackgrounImageUrl: string = '';
    mobileLogoImageUrl: string = '';
    attachableContent: any = null;
    contentUrl: any = '';
    selectedFolderId: any = 1;
    mounted() {
      stores.Setting.getSettings()
        .then((response) => {
          this.settings(response);
        });
      stores.Setting.getSystemLogo().then((response) => {
        this.logo = response;
        this.imageUrl = this.logo.value;
      });
    }
    settings(data: ISetting[]) {
      // @ts-ignore
      for (const index in data) {
        if (data[index].key === 'mobile_login_background') {
          this.mobileLoginBackground = data[index];
        } else if (data[index].key === 'mobile_logo') {
          this.mobileLogo = data[index];
          } else if (data[index].key === 'primary_company_color') {
          this.defaultBG = data[index];
        } else if (data[index].key === 'secondary_company_color') {
          this.secondaryBG = data[index];
        }
      }
      if (this.mobileLoginBackground) {
        this.mobileLoginBackgrounImageUrl = this.mobileLoginBackground.value;
      }
      if (this.mobileLogo) {
        this.mobileLogoImageUrl = this.mobileLogo.value;
      }
      if (this.defaultBG) {
        this.defaultbgColor = this.defaultBG.value;
      }
      if (this.secondaryBG) {
        this.secondarybgColor = this.secondaryBG.value;
      }
    }
    getFilePath(): string {
      return axiosInstance.defaults.baseURL + stores.File.uploadUrl();
    }
    getHeaders() {
      return { 'X-Project': session.project.id };
    }
    updateSetting(id: any, value: any) {
      stores.Setting.update(id, value)
        .then((response) => {
          console.log('setting updated successfully..');
        });
    }
    // open pop-up to create folder or directory
    folderRequest(res: any) {
      this.selectedFolderId = res.folderId;
      // @ts-ignore
      this.$refs.image.$children[0].close();
      // @ts-ignore
      this.$refs.create.$children[0].open();
    }
    // callback method from folder pop-up to create folder
    createFolder(name: any) {
      stores.Folder.createFolder(name, this.selectedFolderId).then((response) => {
        this.selectedFolderId = response.mediaFolderId;
        // @ts-ignore
        this.$refs.create.$children[0].close();
        this.getImages();
      });
    }
    // Logo Setting area
    attachWithImage(res: any) {
      this.imageUrl = res.result.imageUrl;
      // @ts-ignore
      this.$refs.image.$children[0].close();
      this.getImage(res.result.id);
    }
    getImage(id: number) {
      return stores.File.getImage(id)
        .then((response) => {
          this.imageUrl = response.imageUrl;
        })
        .catch((error) => {
          console.log(error);
        });
    }
    getImages() {
      return stores.Folder.getFolder(1)
        .then((response) => {
          this.attachableContent = response;
          this.attachableContent.children = this.attachableContent.folders.concat(
            this.attachableContent.files,
          );
          // @ts-ignore
          this.$refs.image.$children[0].open();
        })
        .catch((error) => {
          console.log(error);
        });
    }
    sendReload(files: any, result: any) {
      this.imageUrl = result.imageUrl;
      this.getImage(result.id);
    }
    // Mobile login background setting area
    attachBackgroundWithImage(res: any) {
      this.mobileLoginBackgrounImageUrl = res.result.imageUrl;
      // @ts-ignore
      this.$refs.loginBackground.$children[0].close();
      this.getBackgroundImage(res.result.id);
    }
    getBackgroundImage(id: number) {
      return stores.File.getImage(id)
        .then((response) => {
          this.mobileLoginBackgrounImageUrl = response.imageUrl;
        })
        .catch((error) => {
          console.log(error);
        });
    }
    getBackgroundImages() {
      return stores.Folder.getFolder(1)
        .then((response) => {
          this.attachableContent = response;
          this.attachableContent.children = this.attachableContent.folders.concat(
            this.attachableContent.files,
          );
          // @ts-ignore
          this.$refs.loginBackground.$children[0].open();
        })
        .catch((error) => {
          console.log(error);
        });
    }
    sendBackgroundReload(files: any, result: any) {
      this.mobileLoginBackgrounImageUrl = result.imageUrl;
      this.getBackgroundImage(result.id);
    }
    // mobile logo setting area
    attachMobileLogoWithImage(res: any) {
      this.mobileLogoImageUrl = res.result.imageUrl;
      // @ts-ignore
      this.$refs.mobileLogo.$children[0].close();
      this.getMobileLogoImage(res.result.id);
    }
    getMobileLogoImage(id: number) {
      return stores.File.getImage(id)
        .then((response) => {
          this.logo = response.imageUrl;
        })
        .catch((error) => {
          console.log(error);
        });
    }
    getMobileLogoImages() {
      return stores.Folder.getFolder(1)
        .then((response) => {
          this.attachableContent = response;
          this.attachableContent.children = this.attachableContent.folders.concat(
            this.attachableContent.files,
          );
          // @ts-ignore
          this.$refs.mobileLogo.$children[0].open();
        })
        .catch((error) => {
          console.log(error);
        });
    }
    sendMobileLogoReload(files: any, result: any) {
      this.mobileLogoImageUrl = result.imageUrl;
      this.getMobileLogoImage(result.id);
    }
    updateLogo() {
      console.log(this.imageUrl);
    }
  }
</script>