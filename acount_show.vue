<template>
  <div class="container">
    <skeleton v-if="!item"/>

    <div v-else>
      <div class="mb-2">
        <router-link to="/accounts" style="color: #637381">
          <span class="fas fa-chevron-left"></span>
          Accounts
        </router-link>
      </div>

      <nevron-header>
        <template #title>{{item.name}}</template>
        <template #nav>
          <li class="nav-item">
            <a class="nav-link pl-0 disabled" href="#"><span class="fas fa-upload mr-2"></span>Import</a>
          </li>
          <li class="nav-item">
            <a class="nav-link pl-0 disabled" href="#"><span class="fas fa-download mr-2"></span>Export</a>
          </li>
          <li>
          </li>
          <li class="nav-item">
            <nevron-click-confirm>
              <router-link class="nav-link pl-0" variant="success"
                           :to="{name: 'accounts.delete', params: {id: $route.params.id}}">
                <span class="fas fa-trash-alt mr-2"></span>Remove
              </router-link>
            </nevron-click-confirm>
          </li>
        </template>
        <template #buttons>
          <router-link v-if="item.neighbours.prev !== null"
                       :to="{name: 'accounts.show', params: {id: item.neighbours.prev}}"
                       class="btn btn-link-gray"><span class="fas fa-arrow-left"></span>
          </router-link>
          <div v-else class="btn btn-link-gray disabled"><span class="fas fa-arrow-left"></span>
          </div>
          <router-link v-if="item.neighbours.next !== null"
                       :to="{name: 'accounts.show', params: {id: item.neighbours.next}}"
                       class="btn btn-link-gray"><span class="fas fa-arrow-right"></span>
          </router-link>
          <div v-else class="btn btn-link-gray disabled"><span class="fas fa-arrow-right"></span>
          </div>
        </template>
      </nevron-header>

      <div class="row">
        <div class="col-lg-8 col-md-12">
          <form @submit.prevent="onSubmit">
            <div class="card mb-4">
              <div class="card-header container-fluid">
                <div class="row">
                  <div class="col-md-10">
                    Account overview
                  </div>
                  <div class="col-md-2 float-right text-right">
                    <div class="custom-control custom-switch">
                      <input type="checkbox" class="custom-control-input" id="active"
                             v-model="item.active" @change="onSubmitStatus()">
                      <label class="custom-control-label" for="active"></label>
                    </div>
                  </div>
                </div>
              </div>
              <div class="card-body">
                <div class="form-group">
                  <p><b>Account ID:</b>{{item.id}}</p>
                </div>
                <div class="form-group">
                  <label for="first-name">Name</label>
<!--                  <input class="col-sm-12 col-xl-12 form-control" name="first-name" id="first-name"-->
<!--                         type="text" v-model="item.name"/>-->
                  <nevron-input  :referenceKey=" 'account' + item.id + '.name'"
                                 v-model="item.name"  name="first-name" id="first-name"/>
                </div>
                <div class="search-content">
                  <p><b>Device limit</b></p>
                  <p>STB/Smart TV:<input class="col-sm-12 col-xl-12 form-control" name="stb-limit"
                                         id="stb-limit" type="text" v-model="item.deviceLimitStb"/>
                  </p>
                  <p>Mobile:<input class="col-sm-12 col-xl-12 form-control" name="mobile-limit"
                                   id="mobile-limit" type="text" v-model="item.deviceLimitMobile"/>
                  </p>
                  <br/>
                  <p><b>Description:</b> no description available</p>
                </div>
              </div>
              <div class="card-footer text-right">
                <button class="btn btn-primary">Update</button>
              </div>
            </div>
          </form>

          <div class="card mb-4">
            <div class="card-header container-fluid">
              <div class="row">
                <div class="col-md-10">
                  Packages
                </div>
                <div class="col-md-2 float-right text-right">
                  <button type="button" class="btn btn-primary text-white btn-sm"
                          @click="fetchPackages({index: null, query: null}); $refs.attachPackage.$children[0].open()">
                    <span class="fas fa-plus"></span></button>
                </div>
              </div>
            </div>
            <div class="card-body" v-if="false">
              <!-- TODO: kle not preglej za pravice od accounta -->
              No data. Add some?
            </div>
            <div class="card-body" v-else>
              <!-- TODO: dodati je treba še en stolpec za sort, tako kot na seznamu kanalov -->
              <table class="table table-hover">
                <thead>
                <tr>
                  <th>Name</th>
                  <th class="text-center">Action</th>
                </tr>
                </thead>
                <tbody v-for="(packageItem, index) in item.packages" :key="packageItem.id">
                <tr>
                  <td>
                    <router-link :to="{name: 'packages.show', params: {id: packageItem.id}}">{{
                      packageItem.name }}
                    </router-link>
                  </td>
                  <td class="text-center">
                    <a href="" @click="detachPackage(packageItem, index, $event)"><span
                      class="fas fa-times text-danger"></span></a>
                  </td>
                </tr>
                </tbody>
              </table>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-header container-fluid">
              <div class="row">
                <div class="col-md-10">
                  Devices
                </div>
                <div class="col-md-2 float-right text-right">
                  <button type="button" class="btn btn-primary text-white btn-sm"
                          @click="fectchDevices({index: null, query: null}); $refs.attach.$children[0].open()">
                    <span class="fas fa-plus"></span></button>
                </div>
              </div>
            </div>
            <div class="card-body">
              <div v-if="deviceError">
                <div class="alert alert-danger" v-if="testButClicked"
                     v-for="fd in deviceErrorResponse.devices" :key="fd.id">
                  Error: {{ fd.message }} ({{ 'Name :' + fd.device.name + ', ' }} {{ 'MAC: ' +
                  fd.device.macEth + ',' }})
                  <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                    <span aria-hidden="true" @click="testToast(fd)">&times;</span>
                  </button>

                </div>
              </div>
              Short explanation of account devices.
            </div>
            <div class="card-body" v-if="item.devices.length === 0">
              <!-- TODO: kle not preglej za pravice od accounta -->
              No data. Add some?
            </div>
            <div class="card-body" v-else>
              <!-- TODO: dodati je treba še en stolpec za sort, tako kot na seznamu kanalov -->
              <table class="table table-hover">
                <thead>
                <tr>
                  <th>Picture</th>
                  <th>MAC</th>
                  <th>Type</th>
                  <th class="text-center">Action</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="(device, index) in item.devices" :key="device.id">
                  <td>
                    <router-link :to="{name: 'devices.show', params: {id: device.id}}"><img
                      class="rounded-circle" style="height: 32px; weight: 32px"
                      src="https://www.w3schools.com/w3images/avatar2.png"/></router-link>
                  </td>
                  <td>
                    <router-link :to="{name: 'devices.show', params: {id: device.id}}">
                      {{device.macEth}}
                    </router-link>
                  </td>
                  <td>
                    <router-link :to="{name: 'devices.show', params: {id: device.id}}">
                      {{device.type.name}}
                    </router-link>
                  </td>
                  <td class="text-center">
                    <a href="" @click="detachDevice(device.id, index, $event)"><span
                      class="fas fa-times text-danger"></span></a>
                  </td>
                </tr>
                </tbody>
              </table>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-header container-fluid">
              <div class="row">
                <div class="col-md-10">
                  Profiles
                </div>
                <div class="col-md-2 float-right text-right">
                  <router-link class="btn btn-primary text-white btn-sm"
                               :to="{name: 'profile.create', params: {id: $route.params.id}}"><span
                    class="fas fa-plus"></span></router-link>
                </div>
              </div>
            </div>
            <div class="card-body">
              Short explanation of account prfiles.
            </div>
            <div class="card-body" v-if="false">
              <!-- TODO: kle not preglej za pravice od accounta -->
              No data. Add some?
            </div>
            <div class="card-body" v-else>
              <!-- TODO: dodati je treba še en stolpec za sort, tako kot na seznamu kanalov -->
              <table class="table table-hover"
                     v-if="item && item.profiles && item.profiles.length > 0">
                <thead>
                <tr>
                  <th>Profile</th>
                  <th>Name</th>
                  <th>PIN</th>
                  <th>Status</th>
                  <th class="text-center">Action</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="(profile, index) in item.profiles" :key="profile.id">
                  <td v-if="profile.imageId && profile.image">
                    <img class="rounded-circle" :src="profile.image.imageUrl"
                         style="height: 32px; wight: 32px;"/>
                  </td>
                  <td v-else>
                    <img class="rounded-circle" src="https://www.w3schools.com/w3images/avatar2.png"
                         style="height: 32px; width: 32px;"/>
                  </td>
                  <td>
                    <router-link
                      :to="{name: 'accounts.profile.show', params:{acc: item.id, id: profile.id}}">
                      {{profile.name}}
                    </router-link>
                  </td>
                  <td>{{profile.pinRequired === 1 ? true : false}}</td>
                  <td>{{ profile.active === 1 ? 'enable' :'disable'}}</td>
                  <td class="text-center">
                    <a href="" @click="removeProfile(profile, index, $event)"><span
                      class="fas fa-times text-danger"></span></a>
                  </td>
                </tr>
                </tbody>
              </table>
            </div>
          </div>

          <div class="card mb-4">
            <div class="card-header container-fluid">
              <div class="row">
                <div class="col-md-10">
                  Users
                </div>
                <div class="col-md-2 float-right text-right">
                  <button type="button" class="btn btn-primary text-white btn-sm"
                          data-backdrop='static' data-keyboard='false'
                          @click="fetchUsers({index: null, query: null}); $refs.user.$children[0].open()">
                    <span class="fas fa-plus"></span></button>
                </div>
              </div>
            </div>
            <div class="card-body">
              Short explanation of account prfiles.
            </div>
            <div class="card-body" v-if="false">
              <!-- TODO: kle not preglej za pravice od accounta -->
              No data. Add some?
            </div>
            <div class="card-body" v-else>
              <!-- TODO: dodati je treba še en stolpec za sort, tako kot na seznamu kanalov -->
              <table class="table table-hover" v-if="item && item.users && item.users.length > 0">
                <tbody>
                <tr v-for="(user, index) in item.users" :key="user.id">
                  <td>
                    <router-link :to="{name: 'users.show', params: {id: user.id}}">{{user.name}}
                    </router-link>
                  </td>
                  <td>{{user.email !== null ? user.email : user.username}}</td>
                  <td><a href="" @click="detachUser(user, index, $event)"><span
                    class="fas fa-times text-danger"></span></a></td>
                </tr>
                </tbody>
              </table>
            </div>
          </div>
          <div class="card mb-4">
            <div class="card-header container-fluid">
              <div class="row">
                <div class="col-md-10">
                  Languages
                </div>
                <div class="col-md-2 float-right text-right">
                  <button type="button" class="btn btn-primary text-white btn-sm"
                          data-backdrop='static' data-keyboard='false'
                          @click="fetchLanguages({index: null, perPage: 10 ,query: ''}); $refs.language.$children[0].open()">
                    <span class="fas fa-plus"></span></button>
                </div>
              </div>
            </div>
            <div class="card-body">
              connected languages for this account.
            </div>
            <div class="card-body" v-if="false">
              <!-- TODO: kle not preglej za pravice od accounta -->
              No data. Add some?
            </div>
            <div class="card-body" v-else>
              <!-- TODO: dodati je treba še en stolpec za sort, tako kot na seznamu kanalov -->
              <table class="table table-hover text-center"
                     v-if="item && item.languages && item.languages.length > 0">
                <thead>
                <tr>
                  <th>Default</th>
                  <th>Flag</th>
                  <th>Language</th>
                  <th>Language Code</th>
                  <th>Action</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="(language, index) in item.languages" :key="language.id">
                  <td class="p-2 align-middle text-center">
                    <label :for="'cb-' + language.id" class="polaris-check" v-if="language">
                      <input
                        type="checkbox"
                        :name="'cb-' + language.id"
                        :value="language.id"
                        v-model="language.pivot.isDefault"
                        @click="changeDefaultLanguage(language.id)"
                      />
                      <span><span class="sr-only">Select Item</span></span>
                    </label>
                  </td>
                  <td>
                    <router-link :to="{name: 'languages.show', params: {id: language.id}}">
                      <img :src="language.flag" :alt="language.name"
                           style="width:50px; height: 40px;">
                    </router-link>
                  </td>
                  <td>
                    <router-link :to="{name: 'languages.show', params: {id: language.id}}">
                      {{language.name}}
                    </router-link>
                  </td>
                  <td>
                    <router-link :to="{name: 'languages.show', params: {id: language.id}}">
                      {{language.shortCode}}
                    </router-link>
                  </td>
                  <td><a href="" @click="detachLanguage(language, index, $event)"><span
                    class="fas fa-times text-danger"></span></a></td>
                </tr>
                </tbody>
              </table>
            </div>
          </div>

          <!--   What is this for??
          <div class="card mb-4">
            <div class="card-header container-fluid">
              <div class="row">
                <div class="col-md-10">
                  Device type
                </div>
                <div class="col-md-2 float-right text-right">
                  <button type="button" class="btn btn-primary text-white btn-sm" @click="fetchUsers({index: null, query: null}); $refs.user.$children[0].open()"><span class="fas fa-plus"></span></button>
                </div>
              </div>
            </div>
            <div v-if="item.deviceType" class="card-body">
              {{item.deviceType.name}}
            </div>
          </div>
          -->

        </div>

        <div class="col-lg-4 col-md-12">
          <div class="card mb-4">
            <div class="card-header container-fluid">
              <div class="row">
                <div class="col-md-10">
                  Owner
                </div>
                <div class="col-md-2 float-right text-right">
                  <a href="" class="btn btn-primary text-white btn-sm" v-if="item.customer"
                     @click="detach($event)"><span class="fas fa-minus"></span></a>
                  <button class="btn btn-primary text-white btn-sm" v-else
                          @click="fetchCustomers({index: null, query: null}); $refs.customer.$children[0].open()">
                    <span class="fas fa-plus"></span></button>
                </div>
              </div>
            </div>
            <div class="card-body">
              <div v-if="item.customer">
                <router-link :to="{name: 'customers.show', params: {id: item.customerId}}">
                  {{item.customer.firstName}} {{item.customer.lastName}}
                </router-link>
                <p v-if="item.customer.firstName && item.customer.lastName"></p>
              </div>
              <b v-else>This account has no owner</b>
            </div>
          </div>

          <!--        <div class="card mb-4">-->
          <!--          <div class="card-header container-fluid">-->
          <!--            <div class="row">-->
          <!--              <div class="col-md-10">-->
          <!--                Location-->
          <!--              </div>-->
          <!--              <div class="col-md-2 float-right text-right">-->
          <!--                <button type="button" class="btn btn-primary text-white btn-sm" ><span class="fas fa-edit"></span></button>-->
          <!--              </div>-->
          <!--            </div>-->
          <!--          </div>-->
          <!--          <div class="card-body">-->
          <!--            &lt;!&ndash; TODO: dodej funkcionalnost lokacije &ndash;&gt;-->
          <!--            <div class="location-info-exist search-content" v-if="true">-->
          <!--              <p>Buckingham street 12, <br />-->
          <!--                11433 London-->
          <!--              </p>-->
          <!--              <img src="../../../assets/nevron.jpg"/>-->
          <!--            </div>-->
          <!--          </div>-->
          <!--        </div>-->

          <div class="card mb-4">
            <div class="card-header container-fluid">
              <div class="row">
                <div class="col-md-10">
                  Activation Code
                </div>
                <div class="col-md-2 float-right text-right">
                  <button type="button" class="btn btn-primary text-white btn-sm"
                          @click="$event.preventDefault(); $refs.reset.$children[0].open()"><span
                    class="fas fa-edit"></span></button>
                </div>
              </div>
            </div>
            <div class="card-body">
              <div class="dej-na-center">
                <b>{{item.activationCode}}</b>
              </div>
              <br/>
              <p style="color: #cccccc;">Activation code is used when a user is registering his STB
                device for the first time.</p>
            </div>
          </div>
        </div>
      </div>
      <attach-device ref="attach" :acc-id="$route.params.id" :full-res="deviceResponse"
                     @save="attachSaveEmited" @refresh="fectchDevices"/>
      <attach-package ref="attachPackage" :acc-id="$route.params.id" :items="packageResponse"
                      @save="attachPackage" @refresh="fetchPackages"/>
      <attach-customer ref="customer" :id="item.id" :full-res="customerResponse"
                       @save="customerSaveEmited" @refresh="fetchCustomers"/>
      <attach-user ref="user" :full-res="userResponse" @save="attachUsers"
                   @refresh="fetchCustomers"/>
      <attach-language ref="language" :full-res="languageResponse" @save="attachLanguages"
                       @refresh="fetchLanguages"/>
      <edit-activation-data ref="reset" :code="item.activationCode" @save="editActivation"/>
    </div>
  </div>
</template>
<script lang="ts">
  import {Component, Vue, Watch} from 'vue-property-decorator';
  import stores from '@/stores';
  import AttachDevice from '@/modules/Devices/Attach.vue';
  import AttachCustomer from '@/modules/Customers/Attach.vue';
  import AttachUser from '@/modules/Users/Attach.vue';
  import AttachLanguage from '@/modules/Languages/Attach.vue';
  import AttachPackage from '@/modules/Packages/AttachPackage.vue';
  import EditActivationData from '@/modules/Accounts/EditActivationCode.vue';
  import Skeleton from '@/modules/Skeleton.vue';
  import NevronHeader from '@/components/NevronHeader.vue';
  import {deletePath} from '../../helpers/DeleteHelper';
  import _ from 'lodash';
  import NevronClickConfirm from '@/components/NevronClickConfirm.vue';
  import Account from '@/stores/Account.ts';
  import NevronInput from '@/components/NevronInput.vue';
  @Component({
    components: {
      AttachDevice,
      AttachCustomer,
      AttachUser,
      AttachPackage,
      EditActivationData,
      Skeleton,
      NevronHeader,
      NevronClickConfirm,
      AttachLanguage,
      NevronInput,
    },
  })
  export default class AccountDetails extends Vue {
    item: IAccount | null = null;
    testButClicked = true;
    deviceResponse: any = null;
    customerResponse: any = null;
    userResponse: any = null;
    packageResponse: any = null;
    searchDevices = _.debounce((res: any) => {
      this.fectchDevices(res);
    }, 400);
    searchCustomers = _.debounce((res: any) => {
      this.fetchCustomers(res);
    }, 400);
    searcUsers = _.debounce((res: any) => {
      this.fetchUsers(res);
    }, 400);
    searcLanguages = _.debounce((res: any) => {
      this.fetchLanguages(res);
    }, 400);
    /*** device Error handling ***/
    deviceError: boolean = false;
    deviceErrorResponse: any = [];
    failedDevices: IDevice[] = [];
    languageResponse: any = false;
    /**
     *  Watches for changes in the route
     */
    @Watch('$route', {immediate: true, deep: true})
    changePage() {
      this.refresh(Number(this.$route.params.id));
    }
    testToast(panels: any) {
      // console.log(this.deviceErrorResponse.devices)
      this.deviceErrorResponse.devices = this.deviceErrorResponse.devices.filter((item: any) => {
        return panels !== item;
      });
      // this.testButClicked = false;
      //
      setTimeout(() => {
        this.testButClicked = false;
      }, 2000);
    }
    /**
     * Sends change to the server when accounts name changes
     */
    onSubmit() {
      if (this.item) {
        return stores.accounts.update(this.item.id, this.item)
          .then((response) => {
            console.log(response);
            console.log('Success');
          })
          .catch((e) => {
            console.log(e);
          });
      }
    }
    /**
     * Sends change to the server when accounts state changes
     */
    onSubmitStatus() {
      if (this.item && this.item.id) {
        return stores.accounts.update(this.item.id, {active: this.item.active})
          .then(() => {
            console.log('success');
          }).catch((e: any) => {
            console.log(e);
          });
      }
    }
    /**
     * Removes account
     */
    popoverMethod() {
      if (this.item && this.item.id) {
        return deletePath(this.item.id);
      }
    }
    /**
     * Sends change to the server when accounts activation code changes
     */
    editActivation(newCode: string) {
      if (this.item) {
        const data = {
          activationCode: newCode,
        };
        return stores.accounts.update(this.item.id, data)
          .then((response) => {
            console.log('Success');
            // @ts-ignore
            this.$refs.reset.$children[0].close();
          })
          .catch((e) => {
            console.log(e);
          });
      }
    }
    /**
     * Gets users on page that can then be attached
     */
    fetchUsers(res: any) {
      return stores.User.fetchData(res.index, res.query, 10)
        .then((response: any) => {
          this.userResponse = response;
        })
        .catch((e: any) => {
          console.log(e);
        });
    }
    /**
     * Gets languages on page that can then be attached
     */
    fetchLanguages(res: any) {
      return stores.accounts.languages(Number(this.$route.params.id), res.index, 10, res.query)
        .then((response: any) => {
          this.languageResponse = response;
          console.log(response, 'working');
        })
        .catch((e: any) => {
          console.log(e);
        });
    }
    /**
     * Attaches the list of languages to this account
     */
    attachLanguages(ids: number[]) {
      return stores.accounts.attachLanguage(ids, Number(this.$route.params.id))
        .then((response: any) => {
          // @ts-ignore
          this.$refs.language.$children[0].close();
          this.refresh(Number(this.$route.params.id));
        })
        .catch((e) => {
          console.log(e);
        });
    }
    changeDefaultLanguage(languageId: any) {
      return stores.accounts.updateLanguageStatus(Number(this.$route.params.id), languageId).then((response: any) => {
        this.refresh(Number(this.$route.params.id));
      }).catch((e: any) => {
        console.log(e);
      });
    }
    /**
     * Attaches the list of users to this account
     */
    attachUsers(ids: number[]) {
      return stores.accounts.attachUser(ids, Number(this.$route.params.id))
        .then((response: any) => {
          // @ts-ignore
          this.$refs.user.$children[0].close();
          this.refresh(Number(this.$route.params.id));
        })
        .catch((e) => {
          console.log(e);
        });
    }
    /**
     * Detaches the selected language from this account
     */
    detachLanguage(language: ILanguage, index: number, e: any) {
      e.preventDefault();
      if (this.item && confirm('Do you really want to detach this Language?')) {
        return stores.accounts.detachLanguage(this.item, language)
          .then((response: any) => {
            if (this.item) {
              this.item.languages.splice(index, 1);
            }
          })
          .catch((error: any) => {
            console.log(error);
          });
      }
    }
    /**
     * Detaches the selected user from this account
     */
    detachUser(user: IUser, index: number, e: any) {
      e.preventDefault();
      if (this.item && confirm('Do you really want to detach this user?')) {
        return stores.accounts.detachUser(this.item, user)
          .then((response: any) => {
            if (this.item) {
              this.item.users.splice(index, 1);
            }
          })
          .catch((error: any) => {
            console.log(error);
          });
      }
    }
    /**
     * Detaches the selected user from this account
     */
    detachPackage(packageItem: IPackage, index: number, e: any) {
      e.preventDefault();
      if (this.item && confirm('Do you really want to detach this package?')) {
        return stores.accounts.detachPackage(this.item, packageItem)
          .then((response: any) => {
            if (this.item) {
              // @ts-ignore
              this.item.packages.splice(index, 1);
            }
          })
          .catch((error: any) => {
            console.log(error);
          });
      }
    }
    /**
     * Removes the desired profile from this accout
     */
    removeProfile(profile: IProfile, index: number, e: any) {
      e.preventDefault();
      if (this.item && profile.id && profile.accountId && confirm('Do you really want to remove this profile?')) {
        return stores.accounts.deleteAccountProfile(profile.id, profile.accountId)
          .then((response) => {
            console.log('Success!');
            if (this.item) {
              this.item.profiles.splice(index, 1);
            }
          })
          .catch((error) => {
            console.log(error);
          });
      }
    }
    /**
     * Detache the specified device from this account
     */
    detachDevice(id: number, index: number, e: any) {
      e.preventDefault();
      if (this.item && this.item.id) {
        return stores.Devices.detachAccount(this.item.id, id)
          .then((response) => {
            console.log('success');
            if (this.item) {
              this.item.devices.splice(index, 1);
            }
          })
          .catch((error) => {
            console.log(error);
          });
      }
    }
    /**
     * Attaches the specified cutomer to this accout
     */
    customerSaveEmited(indexList: number) {
      return stores.accounts.attachCustomer(indexList, Number(this.$route.params.id))
        .then((response) => {
          console.log('Successfully attached customer to this account!');
          // @ts-ignore
          this.$refs.customer.$children[0].close();
          if (this.item) {
            this.item.customerId = indexList;
            this.getOwner();
          }
        })
        .catch((e) => {
          console.log(e);
        });
    }
    /**
     * Searches for customers with the specified query
     */
    fetchCustomers(res: any) {
      return stores.Customer.getAll(res.index, res.query, 10)
        .then((response) => {
          this.customerResponse = response;
        })
        .catch((error) => {
          console.log(error);
        });
    }
    /**
     * Searches for devices with the specified query
     */
    fectchDevices(res: any) {
      return stores.Devices.fetchDeviceData(res.index, res.query, 10)
        .then((response) => {
          console.log(response);
          this.deviceResponse = response;
        })
        .catch((error) => {
          console.log(error);
        });
    }
    fetchPackages(res: any) {
      return stores.Package.getAllPackages()
        .then((response) => {
          this.packageResponse = response;
        })
        .catch((error) => {
          console.log(error);
        });
    }
    /**
     * Attaches sepecified devices to this account
     */
    attachSaveEmited(indexList: number[]) {
      console.log('Emmited IDS', indexList);
      return stores.accounts.attachDevice(indexList, Number(this.$route.params.id))
        .then((response) => {
          if (response.result === false) {
            this.deviceError = true;
            this.deviceErrorResponse = response;
            this.failedDevices = response.devices;
          } else {
            this.deviceError = false;
            this.failedDevices = [];
          }
          console.log('Successfully attached devices with IDs ' + JSON.stringify(response));
          // @ts-ignore
          this.$refs.attach.$children[0].close();
          this.refresh(Number(this.$route.params.id));
          this.fectchDevices({page: null, query: null});
        })
        .catch((e) => {
          console.log(e);
        });
    }
    attachPackage(indexList: number[]) {
      return stores.accounts.attachPackages(indexList, Number(this.$route.params.id))
        .then((response) => {
          console.log('Successfully attached packages with IDs ' + response);
          // @ts-ignore
          this.$refs.attachPackage.$children[0].close();
          stores.accounts.getAccountPackages(this.item != null ? this.item.id : 1)
            .then((packageResponse) => {
              // @ts-ignore
              this.item.packages = packageResponse;
            });
        })
        .catch((e) => {
          console.log(e);
        });
    }
    /**
     * Gets the customer for the specified account
     */
    getOwner() {
      if (this.item && this.item.customerId) {
        return stores.Customer.getById(this.item.customerId)
          .then((response) => {
            console.log(response);
            if (this.item) {
              this.item.customer = response;
            }
          })
          .catch((e) => {
            console.log(e);
          });
      }
    }
    /**
     * Detach the owner of this account
     */
    detach(e: any) {
      e.preventDefault();
      if (this.item && confirm('Do you really want to detach from this customer?')) {
        return stores.accounts.detachCustomer(this.item)
          .then((response: any) => {
            console.log('You have successfully detached this accounts customer');
            if (this.item) {
              this.item.customerId = null;
              this.item.customer = null;
            }
            this.getOwner();
          })
          .catch((error: any) => {
            console.log(error);
          });
      }
    }
    /**
     * Refreshes the data for the currently selected account
     */
    refresh(id: number) {
      return stores.accounts.getSelectedAccount(id)
        .then((response: any) => {
          this.item = response;
          console.log(response);
        })
        .catch((e: any) => {
          console.log(e);
        });
    }
    /**
     * Called when changes need to re-render
     */
    mounted() {
      this.refresh(Number(this.$route.params.id));
    }
    // testToast() {
    //   this.testButClicked = true;
    // }
  }
</script>