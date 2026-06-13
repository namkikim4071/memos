<b-col sm="7" md="6" class="my-1">
<b-table
  :items="items"
  :fields="fields"
  :current-page="currentPage"
  :per-page="perPage"
  :filter="filter"
  :filter-included-fields="filterOn"
  :sort-by.sync="sortBy"
  :sort-desc.sync="sortDesc"
  :sort-direction="sortDirection"
  stacked="md"
  show-empty
  small
  style="font-size: 13px"
  @filtered="onFiltered"
>
  <template #cell(index)="data">
    {{ data.index + 1 }}
  </template>
  <template #cell(company_name)="data">
    <div>
      <b-link @click="clickCompanyNameLink(data)">{{ data.value }}</b-link>
    </div>
  </template>
</b-table>
</b-col>

<b-col sm="7" md="6" class="my-1">
<b-pagination
  v-model="currentPage"
  :total-rows="totalRows"
  :per-page="perPage"
  align="fill"
  size="sm"
  class="my-0"
></b-pagination>
</b-col>
